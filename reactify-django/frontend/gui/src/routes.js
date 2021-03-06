import React from 'react'
import { Route } from 'react-router-dom'
import SubscriptionList from './containers/SubscriptionListView'
import SubscriptionDetail from './containers/SubscriptionDetailView'
import JoinVsChannel from './containers/JoinVsChannel'
import Test from './containers/test'

const BaseRouter = () => (
  <div>
    <Route exact path='/' component={SubscriptionList} />
    <Route exact path={'/:subscriptionID'} component={SubscriptionDetail} />
    <Route exact path={'/deshboard/join-vs-channel'} component={JoinVsChannel} />
    <Route exact path={'/deshboard/subs-status'} component={Test} />
  </div>

)

export default BaseRouter
