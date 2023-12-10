import React, { useState} from 'react'
import { Link } from 'react-router-dom'

export default function MessageInput() {
    const {InputValue, setInputValue} = useState('');
    const handleInputChange = (event) => {
        setInputValue(event.target.value)
    }
    const handleSendMessage = () => {
        console.log("MESSAGE SEND")
    }
    return (
        <div className='message-input'>
            <textarea
                placeholder='Type your message'
                value={InputValue}
                onChange={handleInputChange}
            />
            <button onClick={handleSendMessage}> Send </button>
        </div>
    )
}