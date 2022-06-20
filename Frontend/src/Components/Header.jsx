import React from 'react'
import { Text, Box } from '@chakra-ui/react'

const Header = ({ category, title }) => {
  return (
    <Box
      mb={'15px'}
    >
      <Text
        color={'gray.400'}
      > 
        { category } 
      </Text>
      <Text
        fontWeight={'extrabold'} fontSize={'3xl'} color={'slate-900'}
      > 
        { title } 
      </Text>
    </Box>
  )
}

export default Header