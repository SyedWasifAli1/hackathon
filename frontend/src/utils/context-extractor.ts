/**
 * Utility functions for extracting context from selected text
 */

interface ExtractedContext {
  text: string;
  surroundingText: string;
  sectionTitle: string | null;
  chapterTitle: string | null;
  sourceId: string | null;
}

/**
 * Extracts context from the selected text and its surroundings
 * @param selectedText The text that was selected by the user
 * @param element The DOM element where the selection occurred
 * @returns Extracted context with surrounding information
 */
export const extractContextFromSelection = (selectedText: string, element?: HTMLElement): ExtractedContext => {
  // Default return value
  const defaultContext: ExtractedContext = {
    text: selectedText,
    surroundingText: '',
    sectionTitle: null,
    chapterTitle: null,
    sourceId: null
  };

  if (!element) {
    // If no element provided, try to find context from the current document
    element = document.elementFromPoint(window.innerWidth / 2, window.innerHeight / 2) as HTMLElement;
  }

  if (!element) {
    return defaultContext;
  }

  // Try to find the closest section title (H2, H3, etc.)
  const sectionHeading = element.closest('h1, h2, h3, h4') ||
                         findClosestHeading(element, ['h1', 'h2', 'h3', 'h4']);

  // Try to find surrounding text by getting text from parent containers
  let surroundingText = '';
  let currentElement: HTMLElement | null = element;

  // Look for text in parent elements up to 3 levels up
  for (let i = 0; i < 3 && currentElement; i++) {
    if (currentElement.textContent && currentElement.textContent.trim().length > 0) {
      const elementText = currentElement.textContent.substring(0, 500); // Limit to 500 chars
      if (elementText.includes(selectedText)) {
        // Get the surrounding text, focusing on the area around the selection
        const selectedIndex = elementText.indexOf(selectedText);
        const start = Math.max(0, selectedIndex - 100);
        const end = Math.min(elementText.length, selectedIndex + selectedText.length + 100);
        surroundingText = elementText.substring(start, end).trim();
        break;
      }
    }
    currentElement = currentElement.parentElement;
  }

  // Try to find the chapter title (usually in h1 or an element with specific class)
  const chapterTitleElement = document.querySelector('h1, .chapter-title, .docTitle') as HTMLElement;
  const chapterTitle = chapterTitleElement?.textContent?.trim() || null;

  // Try to extract source ID from data attributes or URL
  const sourceId = element.getAttribute('data-source-id') ||
                  document.querySelector('[data-source-id]')?.getAttribute('data-source-id') ||
                  null;

  return {
    text: selectedText,
    surroundingText: surroundingText || selectedText,
    sectionTitle: sectionHeading?.textContent?.trim() || null,
    chapterTitle: chapterTitle,
    sourceId: sourceId
  };
};

/**
 * Helper function to find the closest heading element
 */
const findClosestHeading = (element: HTMLElement, headingSelectors: string[]): HTMLElement | null => {
  // Look for headings before the current element in the DOM
  const allHeadings = Array.from(document.querySelectorAll(headingSelectors.join(', '))) as HTMLElement[];
  const elementTop = element.getBoundingClientRect().top + window.pageYOffset;

  // Find the closest heading above the element
  for (let i = allHeadings.length - 1; i >= 0; i--) {
    const heading = allHeadings[i];
    const headingTop = heading.getBoundingClientRect().top + window.pageYOffset;

    if (headingTop < elementTop) {
      // Check if the heading is reasonably close to the element
      if (elementTop - headingTop < 500) { // Within 500px
        return heading;
      }
      break; // If the heading is too far, stop searching
    }
  }

  return null;
};

/**
 * Prepares context for RAG query based on selected text
 */
export const prepareContextForRAG = (selectedText: string, element?: HTMLElement): {
  contextText: string;
  sourceId?: string;
  sourceType?: string
} => {
  const context = extractContextFromSelection(selectedText, element);

  // Combine the selected text with surrounding context
  const fullContext = [
    context.chapterTitle && `Chapter: ${context.chapterTitle}`,
    context.sectionTitle && `Section: ${context.sectionTitle}`,
    `Selected text: ${context.text}`,
    context.surroundingText && `Surrounding context: ${context.surroundingText}`
  ].filter(Boolean).join('\n\n');

  return {
    contextText: fullContext,
    sourceId: context.sourceId || undefined,
    sourceType: context.sourceId ? 'textbook_chapter' : undefined
  };
};