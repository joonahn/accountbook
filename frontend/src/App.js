import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import AddAccDataForm from './AddAccDataForm'
import { checkAuthenticated } from './remote'
import PrivateRoute from './PrivateRoute'
import Login from './Login'
import './App.css';
import 'semantic-ui-css/semantic.min.css'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      isAuthenticated: null,
    }
    this.checkLogin()
  }

  checkLogin() {
    checkAuthenticated().then((res) => {
      if (res.status === 200) {
        this.setState({
          isAuthenticated: true
        })
      } else {
        this.setState({
          isAuthenticated: false
        })
      }
    }).catch((err) => {
      console.log("error while checkAuthenticate", err)
      this.setState({
        isAuthenticated: false
      })
    })
  }

  render() {
    return (
      <div className="App">
        <Router basename="/">
          <PrivateRoute path="/" exact
            component={AddAccDataForm}
            checkLogin={this.checkLogin.bind(this)}
            isAuthenticated={this.state.isAuthenticated} />
          <Route path="/login">
            <Login
              isAuthenticated={this.state.isAuthenticated}
              checkLogin={this.checkLogin.bind(this)} />
          </Route>
        </Router>
      </div>
    );
  }
}

export default App;
