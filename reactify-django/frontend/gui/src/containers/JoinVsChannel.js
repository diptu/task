  import React, { Component } from 'react'
import axios from 'axios'
import { Card } from 'antd'
import {HorizontalBar, Pie } from 'react-chartjs-2';

const data = {
  labels: [],
  datasets: [
    {
      label: 'Bar Chart for Subscription Status',
      backgroundColor: [
    '#00FFFF',
    '#FF6384',
    '#36A2EB',
    '#FFCE56',
    '#112f8c',
    '#21618c',
    
    '#008080',
    '#800080',
    '#FF00FF'
    ],
    hoverBackgroundColor: [
    '#00FFFF',
    '#FF6384',
    '#36A2EB',
    '#FFCE56',
    '#112f8c',
    '#21618c',
    '#008080',
    '#800080',
    '#FF00FF'
],
      borderColor: 'rgba(255,99,132,1)',
      borderWidth: 1,
      //hoverBackgroundColor: 'rgba(255,99,132,0.4)',
      hoverBorderColor: 'rgba(255,99,132,1)',
      data: []
    }
  ]
};


class JoinVsChannel extends Component {

   state = {
      items: []
  }

  componentDidMount () {
    axios.get('http://127.0.0.1:8000/api/deshboard/chart')
      .then(response => {
        this.setState({
          items: response.data,

        })
        //console.log(response.data)
      })
   
  }


displayName: 'BarExample';

render () {

    //console.log(this.state.items)  
 // data.labels = 
  //console.log(data.datasets[0].data)
  {this.state.items.map((item,index) =>{
        
        data.labels.push(item.subscription_status);
        data.datasets[0].data.push(item.subscription_status__count)
       
        })
  }


    return (
      
      <Card >
      
      
      
     <div className="row">
      <HorizontalBar data={data} />
      <HorizontalBar data={data} />
      </div>
      </Card>

    )

  //   return (
  //   <React.Fragment>
  //       <h1>Subscription Status </h1>
  //       <HorizontalBar key='1' data={data} />
  //       <Pie key='2' data={data} />
        
  //   </React.Fragment>

  // );
  }
}
export default JoinVsChannel



