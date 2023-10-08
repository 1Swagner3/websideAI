import React, { useState } from 'react';
import sendQuery from '../service/websideAiService';
import ChatHistory from './chatHistory';
import ChatInputForm from './chatInputForm';

function ChatComponent() {
    const [query, setQuery] = useState('');
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      setLoading(true);
      const currentQuery = query;
    
      setMessages(prevMessages => [...prevMessages, { sender: 'user', text: currentQuery }]);

      setQuery('');
    
      const aiResponse = await sendQuery(currentQuery);
      setLoading(false);

      setMessages(prevMessages => [...prevMessages, { sender: 'ai', text: aiResponse }]);
    };
    
    return (
      <div>
        <ChatHistory 
          messages={messages} 
          loading={loading}
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
