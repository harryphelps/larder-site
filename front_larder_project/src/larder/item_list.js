import React, { Component } from 'react';
import DummyData from './dummy_data.json';
import ItemDetail from './item_detail';

class ItemList extends Component {
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
