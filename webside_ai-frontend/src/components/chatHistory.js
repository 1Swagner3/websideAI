import React from 'react';
import '../styles/chatHistory.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCircle } from '@fortawesome/free-solid-svg-icons';

function ChatHistory({ messages, loading }) {
  return (
    <div className="chatHistory">
      {messages.map((message, index) => (
        <div
          key={index}
          className={message.sender}>
          {message.text}
        </div>
      ))}
      {loading && <FontAwesomeIcon
        icon={faCircle}
        style={{ color: 'white' }}
        className='loadingIcon'
      />}
    </div>
  );
}

export default ChatHistory;