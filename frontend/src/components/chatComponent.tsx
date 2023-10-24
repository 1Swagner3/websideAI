import React, { useState } from 'react';
import ChatHistory from './chatHistory';
import ChatInputForm from './chatInputForm';
import sendQuery from '../service/queryAI';
import '../styles/chat-component.css';

type Message = {
  sender: 'user' | 'ai';
  text: string;
};

const ChatComponent: React.FC = () => {
    const [query, setQuery] = useState<string>('');
    const [messages, setMessages] = useState<Message[]>([]);
    const [loading, setLoading] = useState<boolean>(false);
  
    const handleSubmit = async (e: React.FormEvent) => {
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
      <div className='chat-component'>
        <ChatHistory 
          messages={messages} 
          loading={loading}
        />
        <ChatInputForm 
          handleSubmit={handleSubmit}
          setQuery={setQuery}
          query={query} 
          disableInput={loading}
        />
      </div>
    );
}

export default ChatComponent;
