import React, { useState } from 'react';
import InputField from './inputField';
import sendQuery from '../service/websideAiService';

function ChatComponent() {
  const [messages, setMessages] = useState([]);

  const handleQueryChange = (inputValue) => {
    // This will be called whenever the value in the InputField changes
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Fetch the current query from the InputField
    const query = e.target.elements.query.value;

    // Add user message to the list
    setMessages(prevMessages => [...prevMessages, { sender: 'user', text: query }]);

    const aiResponse = await sendQuery(query);
    
    // Add AI's response to the list
    setMessages(prevMessages => [...prevMessages, { sender: 'ai', text: aiResponse }]);
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
        <InputField 
          name="query"
          onChange={handleQueryChange} 
          placeholder="Ask the AI..."
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default ChatComponent;
