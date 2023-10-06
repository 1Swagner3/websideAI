import React, { useState } from 'react';
import sendQuery from '../service/websideAiService';

function ChatComponent() {
    const [query, setQuery] = useState('');
    const [messages, setMessages] = useState([]);
  
    const handleSubmit = async (e) => {
      e.preventDefault();
  
      // Add user message to the list
      setMessages(prevMessages => [...prevMessages, { sender: 'user', text: query }]);
  
      const aiResponse = await sendQuery(query);
      
      // Add AI's response to the list
      setMessages(prevMessages => [...prevMessages, { sender: 'ai', text: aiResponse }]);
      setQuery('');
    };
  
    return (
      <div>
        <div className="chatHistory">
          {messages.map((message, index) => (
            <div key={index} className={message.sender}>
              {message.text}
            </div>
          ))}
        </div>
  
        <form onSubmit={handleSubmit}>
          <input 
            type="text" 
            value={query}
            onChange={e => setQuery(e.target.value)}
            placeholder="Ask the AI..."
          />
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }

export default ChatComponent;
