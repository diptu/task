import React, { Component } from 'react'
import { Pie } from 'react-chartjs-2'

const PieExample = (props) => {
  return (
    <div>
      <h2>Pie Chart</h2>
      <Pie data={props.data}
      />
    </div>
  )
}
export default PieExample
