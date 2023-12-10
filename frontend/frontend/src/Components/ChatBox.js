import React from 'react'
import Message from './Message'
import MessageInput from './MessageInput'

export default function ChatBox() {
    return (
        <div className='chat-box'>
            <div className='chat-header'></div>
            <div className='messages'>
                <Message text="Hey, how" sent/>
                <Message text="I am" received/>
            </div>
            <MessageInput/>

        </div>
    )
}