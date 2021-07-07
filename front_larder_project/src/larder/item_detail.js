import React, { Component } from 'react';

class ItemDetail extends Component {
	render(){
	const p = this.props.p
		return(
			<div>
				<h4>{p.id}. {p.name} - {p.total_in_stock} in stock</h4>
			</div>
		)
	}
}
export default ItemDetail;

