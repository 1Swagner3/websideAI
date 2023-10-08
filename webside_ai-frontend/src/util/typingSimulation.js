function typingSimulation({text, setMessages, prevMessages}) {
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