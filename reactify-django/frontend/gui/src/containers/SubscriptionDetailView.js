import React, { Component } from 'react'
import axios from 'axios'
import { Card , Avatar} from 'antd'

class SubscriptionDetail extends Component {
 
 
    state = {
      item: {}
    }

  componentDidMount () {
  	const subscriptionID = this.props.match.params.subscriptionID;
    axios.get('http://127.0.0.1:8000/api/'+subscriptionID)
      .then(response => {
        this.setState({
          item: response.data

        })
         console.log(response.data);
      })
      console.log(subscriptionID)

  }
  render () {
  	

  
    return (

      <Card >
      {<Avatar src='https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png' />} 
      <p>{this.state.item.membership_no}</p>
      <p>create_date :{this.state.item.create_date}</p>
      <p>subscription_on :{this.state.item.subscription_on}</p>
      <p>current_product_code :{this.state.item.current_product_code}</p>
      <p>previous_product_code :{this.state.item.previous_product_code}</p>
      <p>parent_membership_no :{this.state.item.parent_membership_no}</p>
      <p>subscription_channel :{this.state.item.subscription_channel}</p>
      <p>subscription_on :{this.state.item.subscription_on}</p>
      <p>subscription_status :{this.state.item.subscription_status}</p>
      
      </Card>
    )
  }
}
export default SubscriptionDetail

