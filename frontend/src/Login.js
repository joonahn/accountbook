import React, {Component} from 'react'
import {Form, Dimmer, Loader} from 'semantic-ui-react'
import {authenticate} from './remote'
import { Redirect, withRouter } from 'react-router-dom'

class Login extends Component {
    constructor(props) {
        super(props)
        this.state = {
            id: '',
            pw: '',
        }
    }

   onChange(_, {name, value}) {
        this.setState({
            [name]: value
        })
    }

    onSubmit() {
        console.log(this.props)
        authenticate(this.state.id, this.state.pw).then((res) => {
            if (res.status === 200) {
                console.log('authentication succeeded')
                this.props.checkLogin()
            } 
        })
    }

    render() {
        let {from} = this.props.location.state || {from: {pathname:"/"}}
        if (this.props.isAuthenticated) return <Redirect to={from} />
        return (
            <Form onSubmit={this.onSubmit.bind(this)}>
                <Dimmer active={this.props.isAuthenticated === null} inverted>
                    <Loader active={this.props.isAuthenticated === null}/>
                </Dimmer>
                <Form.Input label='Id' name='id' onChange={this.onChange.bind(this)}/>
                <Form.Input label='Password' name='pw' type='password' onChange={this.onChange.bind(this)}/>
                <Form.Button content='Login' />
                {/* <pre>{JSON.stringify(this.state.id)}</pre>
                <pre>{JSON.stringify(this.state.pw)}</pre> */}
            </Form>
        )
    }
}

export default withRouter(Login)