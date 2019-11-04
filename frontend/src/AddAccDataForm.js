import React, { Component } from 'react';
import { addAccountBookData, getAccountList, getCategoryList } from './remote'
import { Form } from 'semantic-ui-react'
import Moment from 'moment'
import 'semantic-ui-css/semantic.min.css'

class AddAccDataFrom extends Component {
    constructor(props) {
        super(props)
        this.state = {
            account_options: [],
            category_options: [],
            inout_options: [
                {key: "income", text: "income", value: "income"},
                {key: "expenditure", text: "expenditure", value: "expenditure"}
            ],
            formData: {
                account_date: Moment(new Date()).format("YYYY-MM-DD"),
                category: "",
                content: "",
                inout: "",
                account: "",
                amount: 0,
            }
        }
    }

    componentDidMount() {
        getAccountList().then((res) =>
            res.map((value) => ({ key: value.id, text: value.account_name, value: value.id }))
        ).then((res) => {
            this.setState({
                account_options: res
            })
        })

        getCategoryList().then((res) => 
            res.map((value) => {
                let text = "--".repeat(value.level) + value.name
                return ({ key: value.id, text: text, value: value.id })
            })
        ).then((res) => {
            this.setState({
                category_options: res
            })
        })
    }

    handleChange = (e, { name, value }) => {
        this.setState({ formData: { ...this.state.formData, [name]: value } })
        console.log(name, value)
    }

    handleClick() {
        console.log("formdata:", this.state.formData)
        addAccountBookData(this.state.formData).then((res) => {
            console.log(res)
            alert("succeeded res:" + String(res.status))
        }).catch((err) => {
            console.log(err)
            alert("failed err:" + String(err.message))
        })
    }

    render() {
        return (
            <Form>
                <Form.Input label='date' name='account_date' type='date' value={this.state.formData.account_date} onChange={this.handleChange}/>
                <Form.Select label='category' name='category' value={this.state.formData.category} options={this.state.category_options} onChange={this.handleChange}/>
                <Form.Input label='content' name='content' type='text' value={this.state.formData.content} onChange={this.handleChange}/>
                <Form.Select label='inout' name='inout' value={this.state.formData.inout} options={this.state.inout_options} onChange={this.handleChange}/>
                <Form.Select label='account' name='account' value={this.state.formData.account} options={this.state.account_options} onChange={this.handleChange}/>
                <Form.Input label='amount' name='amount' type='number' value={this.state.formData.amount} onChange={this.handleChange}/>
                <Form.Button onClick={this.handleClick.bind(this)}>Submit</Form.Button>
            </Form>
        )
    }
}

export default AddAccDataFrom