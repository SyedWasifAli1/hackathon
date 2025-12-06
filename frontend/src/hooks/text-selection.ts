import { useState, useEffect, useCallback } from 'react';

interface TextSelection {
  text: string;
  range: Range | null;
  rect: DOMRect | null;
}

const useTextSelection = () => {
  const [selection, setSelection] = useState<TextSelection>({
    text: '',
    range: null,
    rect: null
  });
  const [isVisible, setIsVisible] = useState(false);

  const getSelectedText = useCallback((): TextSelection => {
    const selection = window.getSelection();

    if (!selection || selection.toString().trim() === '') {
      return { text: '', range: null, rect: null };
    }

    const selectedText = selection.toString().trim();

    if (selectedText.length === 0) {
      return { text: '', range: null, rect: null };
    }

    // Get the range of the selection
    const range = selection.getRangeAt(0);
    const rect = range.getBoundingClientRect();

    return {
      text: selectedText,
      range,
      rect: {
        x: rect.x,
        y: rect.y,
        width: rect.width,
        height: rect.height,
        top: rect.top,
        right: rect.right,
        bottom: rect.bottom,
        left: rect.left
      } as DOMRect
    };
  }, []);

  const handleSelection = useCallback(() => {
    const newSelection = getSelectedText();

    if (newSelection.text) {
      setSelection(newSelection);
      setIsVisible(true);
    } else {
      setIsVisible(false);
    }
  }, [getSelectedText]);

  useEffect(() => {
    document.addEventListener('mouseup', handleSelection);
    document.addEventListener('keyup', handleSelection);

    return () => {
      document.removeEventListener('mouseup', handleSelection);
      document.removeEventListener('keyup', handleSelection);
    };
  }, [handleSelection]);

  const clearSelection = useCallback(() => {
    const selection = window.getSelection();
    if (selection) {
      selection.removeAllRanges();
    }
    setIsVisible(false);
    setSelection({ text: '', range: null, rect: null });
  }, []);

  return {
    selection: selection.text,
    selectionRect: selection.rect,
    isVisible,
    clearSelection,
    getSelectedText
  };
};

export default useTextSelection;