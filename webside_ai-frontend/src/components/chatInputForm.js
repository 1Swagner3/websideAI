import React from 'react';
import '../styles/inputForm.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPaperPlane } from '@fortawesome/free-solid-svg-icons';
function ChatInputForm({query, setQuery, handleSubmit}) {

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={query}
        onChange={e => setQuery(e.target.value)}
        placeholder="Ask the AI..."
        className='inputField'
      />
      <button  
        type="submit"
        className='submitButton'>
          <FontAwesomeIcon icon={faPaperPlane} style={{color: 'white'}}/>
        </button>
    </form>
  );
}

export default ChatInputForm;