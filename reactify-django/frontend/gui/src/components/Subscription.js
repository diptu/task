import React from 'react'

import { List, Avatar, Icon } from 'antd'

const Subscription = (props) => {
  return (

    <List
      itemLayout='vertical'
      size='large'
      pagination={{
        onChange: (page) => {
          console.log(page)
        },
        pageSize: 3
      }}
      dataSource={props.data}

      renderItem={item => (
        <List.Item
          key={item.id}

        >
          <List.Item.Meta
            avatar={<Avatar src='https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png' />}

          />
          <a href={item.id}>{item.membership_no}</a>
          <li>Subscription On : {item.subscription_on} </li>

          <li> Previous Product Code :{item.previous_product_code}</li>
          <li>Previous Product Code : {item.current_product_code}</li>
          <li>Payment type : {item.payment_type}</li>
          <li>Retailer type: {item.retailer_type}</li>
          <li>Subscription Status : {item.subscription_status}</li>
        </List.Item>
      )}
    />
  )
}
export default Subscription
