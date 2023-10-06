import React, { useState } from 'react';

const InputField = ({ onChange, placeholder }) => {
    const [value, setValue] = useState('');

    const handleChange = (e) => {
        const inputValue = e.target.value;
        setValue(inputValue);

        if (onChange) {
            onChange(inputValue);
        }
    }

    return (
        <input
            type="text"
            value={value}
            onChange={handleChange}
            placeholder={placeholder}
        />
    );
}

export default InputField;
