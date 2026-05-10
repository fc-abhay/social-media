"use client"
import { store } from '@/store/store'
import React from 'react'
import { Provider } from 'react-redux'

interface Wrapper{
    children:React.ReactNode
}
const Wrapper:React.FC<Wrapper> = ({children}) => {
  return (
    <Provider store={store}>
        {children}
    </Provider>
  )
}

export default Wrapper