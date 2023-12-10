import React, { useEffect, useState} from 'react'
import { Link } from 'react-router-dom'
import UserItem from './UserItem'
import axios from 'axios';
import { Box, List, LinearProgress } from '@mui/material'

export default function Sidebar() {
    const BASE_URL = `http://127.0.0.1:8000/`
    const [userList, setUserList] = useState([])
    const [userLoader, setUserLoader] = useState(true)
    // cookies
    const getAuthToken = () => {
        const cookies  = document.cookie.split(';')
        for (const cookie in cookies) {
            const [name, value] = cookie.trim().split("=")
            if (name === "token"){
                return value
            }
        }
        return null
    }

    useEffect(() => {
        const authToken = getAuthToken()
        if (authToken) {
            axios.get(`${BASE_URL}api/users/`, {
                headers:{
                    Authorisation:`Bearer ${authToken}`
                }
            }).then(response => {
                setUserList(response.data.data)
                setUserLoader(false)
                console.log(userList);
            }).catch(error => {
                console.log("error making request", error)
            })
        }
    }, [])
    return (
        <div className='sidebar'>
            {userLoader ? (<Box sx={{width: '100%'}}>
                <LinearProgress/>
            </Box>):
            (<List sx={{width: '100%', maxWidth: 360, bgcolor: 'background.paper'}}>
                {userList.map((user, index) => (
                    <UserItem key={index} email={user.email} name={`${user.first_name} ${user.last_name}`} id={user.id}></UserItem>
                ))}
            </List>)
            }
        </div>
    )
}