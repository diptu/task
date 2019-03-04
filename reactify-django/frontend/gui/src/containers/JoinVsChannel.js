import React, { Component } from 'react'
import { Canvas } from 'react-canvas-js'
import axios from 'axios'


class JoinVsChannel extends Component {
   state = {
      items: []
    }

  componentDidMount () {
    axios.get('http://127.0.0.1:8000/api/deshboard/join-vs-channel')
      .then(response => {
        this.setState({
          items: response.data,
        })
      })
  }
  render () {

  console.log(this.state.items)
    return (
        <div>Loded</div>
      )
  }
}
export default JoinVsChannel
