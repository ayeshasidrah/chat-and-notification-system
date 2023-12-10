import logo from './logo.svg';
import './App.css';
import Navigate from './Components/Navigate';
import Login from './Components/Login';
import Register from './Components/Register';
import Sidebar from './Components/Sidebar';
import ChatBox from './Components/ChatBox';
import * as ReactDOM from "react-dom";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Routes,
} from 'react-router-dom';
import React, { useState } from 'react';
import {TextField, Button} from '@mui/material';


function App() {
  return (
    <>
        <div className='App'>
            <Navigate />
            <Routes>
                  <Route path="/register" element={<Register />} />
                  <Route path="/login" element={<Login />} />
                  <Route path="/chat" element={<><div className='chat-container'><Sidebar /><ChatBox /></div></>} />
            </Routes>

        </div>
    </>
  );
};

export default App;
