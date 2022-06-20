import { ChakraProvider } from '@chakra-ui/react'
import React from 'react'
import { Box } from '@chakra-ui/react'
import './App.css'
import Calendar from './Components/Calendar'



const App = () => {
  return (
    <ChakraProvider>
      <Box
        position={'absolute'}
        top={'90'}
        left={'250'}
        right={'50'}
      >
        <Calendar />
      </Box>
    </ChakraProvider>
  )
}

export default App