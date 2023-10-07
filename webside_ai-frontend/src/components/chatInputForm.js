import React from 'react';

function ChatInputForm({query, setQuery, handleSubmit}) {

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={query}
        onChange={e => setQuery(e.target.value)}
        placeholder="Ask the AI..."
      />
      <button type="submit">Submit</button>
    </form>
  );
}

export default ChatInputForm;