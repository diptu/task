import React from 'react'
import axios from 'axios'
import BarExample from '../components/Bar'
import PieExample from '../components/Pie'

var backgroundColor =  ['#00FFFF','#FF6384','#36A2EB','#FFCE56','#112f8c','#21618c','#008080', '#800080', '#FF00FF' ]
var  hoverBackgroundColor = ['#00FFFF','#FF6384','#36A2EB','#FFCE56','#112f8c','#21618c','#008080','#800080','#FF00FF']
var     borderColor = 'rgba(255,99,132,1)'
var     borderWidth = 1
var   hoverBackgroundColor = hoverBackgroundColor
var   hoverBorderColor= 'rgba(255,99,132,1)'
const data_bar = {
  labels: [],
  datasets: [
    {
      label: 'Bar Chart for Subscription Status',
      backgroundColor : backgroundColor,
      borderColor: borderColor,
      borderWidth: borderWidth,
      hoverBackgroundColor : hoverBackgroundColor,
      hoverBorderColor: hoverBorderColor,
      data: []
    }
  ]
};



const data_pie = {
  labels: [],
  datasets: [
    {
      label: 'Pie Chart for Subscription Status',
      backgroundColor : backgroundColor,
      borderColor: borderColor,
      borderWidth: borderWidth,
      hoverBackgroundColor : hoverBackgroundColor,
      hoverBorderColor: hoverBorderColor,
      data: []
    }
  ]
};


class Test extends React.Component {

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
  render () {

  	{this.state.items.map((item,index) =>{
        
        data_bar.labels.push(item.subscription_status);
        data_bar.datasets[0].data.push(item.subscription_status__count);

        data_pie.labels.push(item.subscription_status);
        data_pie.datasets[0].data.push(item.subscription_status__count);
       
        })
  }



    return (
      <div>

        <PieExample data={data_pie}/>

        <BarExample  data={data_bar}/>
      </div>
    )
  }
}
export default Test
