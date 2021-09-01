import axios from 'axios';
import React, { Component } from 'react';
import ItemDetail from './item_detail';
import ItemForm from './itemform';

class ItemList extends Component {
	
	constructor(props) {
		super(props);
		this.state = {
			itemData: [],
			item: " ",
			showComponent: false,
		};
		this.getItemDetail=this.getItemDetail.bind(this);
		this.showItemDetails=this.showItemDetails.bind(this);
	}

	getItemDetail(item) {
	axios.get("http://127.0.0.1:8000/".concat(item.absolute_url))
		.then((response) => {
			this.setState({item: response.data})
		})
		.catch(function (error){
			console.log(error);
		});
	}

	showItemDetails(item) {
		this.getItemDetail(item);
		this.setState({showComponent: true});
	}

	componentDidMount(){
		axios.get("http://127.0.0.1:8000/")
		.then((response) => {
		this.setState({itemData: response.data})
		})
		.catch(function (error) {
		console.log(error);
	})
	}

	render(){
		return(
			<div>
				{this.state.itemData.map((item) => {
				return (<h3 key={item.id} onClick= {() => this.showItemDetails(item)}>
						{item.name}, {item.total_in_stock}
						</h3>
					);
				})}
			{this.state.showComponent ? (
				<ItemDetail itemDetail={this.state.item} /> 
			) : null}
			<ItemForm/>
			</div>
			);
		}
}



export default ItemList;
