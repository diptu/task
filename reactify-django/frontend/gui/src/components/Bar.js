import React, { Component } from 'react'
import { Bar } from 'react-chartjs-2'

const BarExample = (props) => {
  return (
    <div>
      <h2>Bar Chart</h2>
      <Bar
        data={props.data}
        height={150}
        options={{
          maintainAspectRatio: false
        }}
      />
    </div>
  )
}
export default BarExample
