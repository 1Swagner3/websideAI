import React, { useState } from 'react';
import sendQuery from '../service/websideAiService';
import ChatHistory from './chatHistory';
import ChatInputForm from './chatInputForm';

function ChatComponent() {
    const [query, setQuery] = useState('');
    const [messages, setMessages] = useState([]);
  
    const handleSubmit = async (e) => {
      e.preventDefault();

      const currentQuery = query;
    
      setMessages(prevMessages => [...prevMessages, { sender: 'user', text: currentQuery }]);

      setQuery('');
    
      const aiResponse = await sendQuery(currentQuery);

      setMessages(prevMessages => [...prevMessages, { sender: 'ai', text: aiResponse }]);
    };
    
    return (
      <div>
        <ChatHistory 
          messages={messages} 
        />
        <ChatInputForm 
          handleSubmit={handleSubmit}
          setQuery={setQuery}
          query={query} 
        />
      </div>
    );
  }

export default ChatComponent;
