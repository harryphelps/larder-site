import React, { Component } from "react";
import axios from "axios";

class ItemForm extends Component {
	//This is the create form
	constructor(props) {
		super(props);
		this.state = {
			item_name: " ",
			total_in_stock: 0,
			last_purchased_on: " ",
			last_used_on: " ",
			average_shelf_life: 7}
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
			name: this.state.item_name, 
			total_in_stock: this.state.total_in_stock,
			last_purchased_on: this.state.last_purchased_on,
			last_used_on: this.state.last_used_on,
			average_shelf_life: this.state.average_shelf_life,
		})
		.then((response) =>{
			console.log(response);
		})
		.catch(function (error) {
			console.log(error);
		});
	}
	render(){
		const {item_name, total_in_stock, last_purchased_on, last_used_on, average_shelf_life } = this.state;
		return (
			<form onSubmit={this.handleSubmit}>
				<div>
					<div>
					<p>Name:</p>
					<input type="text" name="item_name" value={item_name} onChange={this.handleChange} />
					</div>
					<div>
					<p>Total in stock:</p>
					<input type="number" name="total_in_stock" value={total_in_stock} onChange={this.handleChange} />
					</div>
					<div>
					<p>Last purchased on:</p>
					<input type="date" name="last_purchased_on" value={last_purchased_on} onChange={this.handleChange} />
					</div>
					<div>
					<p>Last used on:</p>
					<input type="date" name="last_used_on" value={last_used_on} onChange={this.handleChange} />
					</div>
					<div>
					<p>Average shelf life:</p>
					<input type="number" name="average_shelf_life" value={average_shelf_life} onChange={this.handleChange} />
					</div>
				</div>
				<input type="submit" value="Submit" />
			</form>
		);
	}
}

export default ItemForm;
