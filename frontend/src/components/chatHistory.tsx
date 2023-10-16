import React, { useEffect, useState } from 'react';
import '../styles/chatHistory.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCircle } from '@fortawesome/free-solid-svg-icons';

type Message = {
  sender: 'user' | 'ai';
  text: string;
};

type ChatHistoryProps = {
  messages: Message[];
  loading: boolean;
};

const ChatHistory: React.FC<ChatHistoryProps> = ({ messages, loading }) => {
  const [typingResponse, setTypingResponse] = useState<string>('');
  const [typing, setTyping] = useState<boolean>(false);

  useEffect(() => {
    const lastMessage = messages[messages.length - 1];

    if (lastMessage && lastMessage.sender === 'ai' && !typingResponse) {
      setTyping(true);

      let aiResponse = lastMessage.text;
      let index = -1;

      const interval = setInterval(() => {
        if (index < aiResponse.length) {
          setTypingResponse(prev => prev + aiResponse.charAt(index));
          index++;
        } else {
          setTyping(false);
          clearInterval(interval);
        }
      }, 50);

      return () => clearInterval(interval);
    }
    setTypingResponse('');
  }, [messages]);

  return (
    <div className="chatHistory">
      {messages.map((message, index) => {
        if (message.sender === 'user') {
          return (
            <div className="user" key={index}>
              <span>{message.text}</span>
            </div>
          );
        } else if (index !== messages.length - 1 || !typing) {
          return (
            <div className="ai" key={index}>
              <span>{message.text}</span>
            </div>
          );
        }
        return null;
      })}
      {typing && <span className="typingEffect ai">{typingResponse}</span>}
      {loading && <FontAwesomeIcon icon={faCircle} style={{ color: 'white' }} className='loadingIcon'/>}
    </div>
  );
}

export default ChatHistory;
