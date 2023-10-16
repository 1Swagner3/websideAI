type Message = {
    sender: 'user' | 'ai';
    text: string;
  };
  
  type TypingSimulationParams = {
    text: string;
    setMessages: React.Dispatch<React.SetStateAction<Message[]>>;
    prevMessages: Message[];
  };
  
  function typingSimulation({ text, setMessages, prevMessages }: TypingSimulationParams) {
      let index = -1;
      const interval = setInterval(() => {
          if (index < text.length) {
              setMessages(prevMessages => [...prevMessages, { sender: 'ai', text: text.charAt(index) }]);
              index++;
          } else {
              clearInterval(interval);
          } 
      }, 50);
  }
  
  export default typingSimulation;
  