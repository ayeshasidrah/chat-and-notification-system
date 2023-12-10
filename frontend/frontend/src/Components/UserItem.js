import React from 'react'
import { ListItem, ListItemText } from '@mui/material'

export default function UserItem(props) {
    return (
        <ListItem>
            <ListItemText primary={props.name} secondary={props.email}></ListItemText>
        </ListItem>
    )
}