import axios from 'axios';
import React, { Component } from 'react';
import DummyData from './dummy_data.json';
import ItemDetail from './item_detail';

class ItemList extends Component {
	componentDidMount(){
		axios.get("http://127.0.0.1:8000/")
		.then((response) => {
		console.log(response)
		})
	.catch(function (error) {
		console.log(error);
	})
	}
	render(){
		return(
			<div>
				{DummyData.map( item => {
				return <ItemDetail p ={item}/>
					})
				}
			</div>
			)
	}
}
export default ItemList;
