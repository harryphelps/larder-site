import React, { Component } from "react";
import axios from "axios";

class ItemForm extends Component {
	constructor(props) {
		super(props);
		this.state = {
			item_name: " "
		};
		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
	}
	handleChange(event) {
		this.setState({[event.target.name]:event.target.value});
	}
	handleSubmit(event) {
		// Prevents accidental clicks
		event.preventDefault();
		console.log(this.state.item_name);
		axios.post("http://127.0.0.1:8000/create/",{
			name: this.state.item_name
		})
		.then((response) =>{
			console.log(response);
		})
		.catch(function (error) {
			console.log(error);
		});
	}
	render(){
		const {item_name } = this.state;
		return (
			<form onSubmit={this.handleSubmit}>
				<div>
					<input type="text" name="item_name" value={item_name} onChange={this.handleChange} />

				</div>
				<input type="submit" value="Submit" />
			</form>
		);
	}
}

export default ItemForm;
