import React from 'react'
import { Flex } from '@chakra-ui/react'
import { ScheduleComponent, Day, Week, WorkWeek, 
    Month, Agenda, Inject, Resize, DragAndDrop } from '@syncfusion/ej2-react-schedule'
import Header from './Header'

const Calendar = () => {
  return (
   <Flex 
      flexDirection={'column'} 
      gap={'5px'} 
      m={{ md: '10px', lg: '2px' }} 
      padding={'20px'}
      bg={'white'} 
      border={'1px'}
      borderColor={'white'}
      borderRadius={'3xl'} 
    >
        <Header category='App' title='Calendar' />
        <ScheduleComponent
          height={'650px'}
        >
            <Inject 
            services={[Day, Week, Month, WorkWeek, Agenda, Resize, DragAndDrop]}
            />
        </ScheduleComponent>
   </Flex>
  )
}

export default Calendar