import React, { Component } from 'react';

class ItemDetail extends Component {
	render(){
	const obj = this.props.itemDetail
		return(
			<div style={{ color: "yellow", border: "1px solid yellow"}}>
				<h4>{obj.id}. {obj.name} - {obj.total_in_stock} in stock</h4>
			</div>
		)
	}
}
export default ItemDetail;

