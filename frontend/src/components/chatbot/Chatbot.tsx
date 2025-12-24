import React, { useState, useRef, useEffect } from 'react';
import { useColorMode } from '@docusaurus/theme-common';

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'bot';
  timestamp: Date;
}

interface ChatbotProps {
  contextText?: string; // Optional context from selected text
}

const Chatbot: React.FC<ChatbotProps> = ({ contextText = '' }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      text: 'Hello! I\'m your AI assistant. How can I help you today?',
      sender: 'bot',
      timestamp: new Date(),
    }
  ]);
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);
  const { colorMode } = useColorMode();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async () => {
    if (!inputText.trim() || isLoading) return;

    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      text: inputText,
      sender: 'user',
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInputText('');
    setIsLoading(true);

    try {
      // Call the external API
      const response = await fetch('https://rag-agent-chatbot-production.up.railway.app/ask', {
          method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: inputText
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      // Add bot response
      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: typeof data === 'string' ? data : (data.response || data.answer || 'I couldn\'t generate a response.'),
        sender: 'bot',
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: 'Sorry, I encountered an error processing your request. Please try again.',
        sender: 'bot',
        timestamp: new Date(),
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  return (
    <>
      {/* Chatbot toggle button */}
      <button
        onClick={toggleChat}
        className={`chatbot-toggle-button ${
          colorMode === 'dark' ? 'chatbot-toggle-button--dark' : 'chatbot-toggle-button--light'
        }`}
        style={{
          position: 'fixed',
          bottom: '20px',
          right: '20px',
          width: '60px',
          height: '60px',
          borderRadius: '50%',
          border: 'none',
          backgroundColor: '#3b82f6',
          color: 'white',
          fontSize: '24px',
          cursor: 'pointer',
          zIndex: 1000,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
        }}
      >
        💬
      </button>

      {/* Chatbot window */}
      {isOpen && (
        <div
          className={`chatbot-window ${
            colorMode === 'dark' ? 'chatbot-window--dark' : 'chatbot-window--light'
          }`}
          style={{
            position: 'fixed',
            bottom: '90px',
            right: '20px',
            width: '400px',
            height: '500px',
            backgroundColor: colorMode === 'dark' ? '#1e293b' : '#ffffff',
            border: `1px solid ${colorMode === 'dark' ? '#334155' : '#e2e8f0'}`,
            borderRadius: '8px',
            boxShadow: '0 10px 25px rgba(0, 0, 0, 0.15)',
            zIndex: 1000,
            display: 'flex',
            flexDirection: 'column',
            fontFamily: 'Inter, sans-serif',
          }}
        >
          {/* Chat header */}
          <div
            style={{
              padding: '16px',
              backgroundColor: colorMode === 'dark' ? '#0f172a' : '#f1f5f9',
              borderTopLeftRadius: '8px',
              borderTopRightRadius: '8px',
              borderBottom: `1px solid ${colorMode === 'dark' ? '#334155' : '#e2e8f0'}`,
              display: 'flex',
              alignItems: 'center',
            }}
          >
            <div
              style={{
                width: '12px',
                height: '12px',
                borderRadius: '50%',
                backgroundColor: '#10b981',
                marginRight: '12px',
              }}
            />
            <h3
              style={{
                margin: 0,
                fontSize: '16px',
                fontWeight: 600,
                color: colorMode === 'dark' ? '#f1f5f9' : '#1e293b',
              }}
            >
              AI Assistant
            </h3>
          </div>

          {/* Chat messages */}
          <div
            style={{
              flex: 1,
              padding: '16px',
              overflowY: 'auto',
              backgroundColor: colorMode === 'dark' ? '#0f172a' : '#f8fafc',
            }}
          >
            {messages.map((message) => (
              <div
                key={message.id}
                style={{
                  display: 'flex',
                  justifyContent: message.sender === 'user' ? 'flex-end' : 'flex-start',
                  marginBottom: '16px',
                }}
              >
                <div
                  style={{
                    maxWidth: '80%',
                    padding: '12px 16px',
                    borderRadius: '18px',
                    backgroundColor:
                      message.sender === 'user'
                        ? colorMode === 'dark' ? '#3b82f6' : '#dbeafe'
                        : colorMode === 'dark' ? '#334155' : '#e2e8f0',
                    color: message.sender === 'user'
                      ? colorMode === 'dark' ? '#ffffff' : '#1e40af'
                      : colorMode === 'dark' ? '#f1f5f9' : '#1e293b',
                    fontSize: '14px',
                    lineHeight: '1.5',
                  }}
                >
                  {message.text}
                </div>
              </div>
            ))}
            {isLoading && (
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'flex-start',
                  marginBottom: '16px',
                }}
              >
                <div
                  style={{
                    maxWidth: '80%',
                    padding: '12px 16px',
                    borderRadius: '18px',
                    backgroundColor: colorMode === 'dark' ? '#334155' : '#e2e8f0',
                    color: colorMode === 'dark' ? '#f1f5f9' : '#1e293b',
                    fontSize: '14px',
                    lineHeight: '1.5',
                  }}
                >
                  Thinking...
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Chat input */}
          <div
            style={{
              padding: '16px',
              backgroundColor: colorMode === 'dark' ? '#0f172a' : '#ffffff',
              borderBottomLeftRadius: '8px',
              borderBottomRightRadius: '8px',
              borderTop: `1px solid ${colorMode === 'dark' ? '#334155' : '#e2e8f0'}`,
            }}
          >
            <div style={{ display: 'flex', gap: '8px' }}>
              <textarea
                ref={inputRef}
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Type your message..."
                style={{
                  flex: 1,
                  padding: '12px',
                  borderRadius: '20px',
                  border: `1px solid ${colorMode === 'dark' ? '#334155' : '#cbd5e1'}`,
                  backgroundColor: colorMode === 'dark' ? '#1e293b' : '#ffffff',
                  color: colorMode === 'dark' ? '#f1f5f9' : '#1e293b',
                  resize: 'none',
                  minHeight: '50px',
                  maxHeight: '100px',
                  fontSize: '14px',
                }}
                rows={1}
              />
              <button
                onClick={handleSendMessage}
                disabled={isLoading || !inputText.trim()}
                style={{
                  padding: '12px 20px',
                  borderRadius: '20px',
                  border: 'none',
                  backgroundColor: inputText.trim() && !isLoading ? '#3b82f6' : '#94a3b8',
                  color: 'white',
                  cursor: inputText.trim() && !isLoading ? 'pointer' : 'not-allowed',
                  fontSize: '14px',
                  fontWeight: 500,
                }}
              >
                Send
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default Chatbot;