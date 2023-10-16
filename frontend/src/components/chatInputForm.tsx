import React, { FormEvent, ChangeEvent } from 'react';
import '../styles/inputForm.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPaperPlane } from '@fortawesome/free-solid-svg-icons';

type ChatInputFormProps = {
  query: string;
  setQuery: (value: string) => void;
  handleSubmit: (event: FormEvent) => void;
  disableInput: boolean;
};

const ChatInputForm: React.FC<ChatInputFormProps> = ({ query, setQuery, handleSubmit, disableInput }) => {
  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={query}
        onChange={(e: ChangeEvent<HTMLInputElement>) => setQuery(e.target.value)}
        placeholder="Ask the AI..."
        className='inputField'
        disabled={disableInput}
      />
      <button  
        type="submit"
        className='submitButton'>
          <FontAwesomeIcon icon={faPaperPlane} style={{ color: 'white' }} />
        </button>
    </form>
  );
}

export default ChatInputForm;
