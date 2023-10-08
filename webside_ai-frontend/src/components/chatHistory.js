import React from 'react';
import '../styles/chatHistory.css';

function ChatHistory({ messages }) {
  return (
    <div className="chatHistory">
      {messages.map((message, index) => (
        <div 
          key={index} 
          className={message.sender}>
          {message.text}
        </div>
      ))}
    </div>
  );
}

export default ChatHistory;