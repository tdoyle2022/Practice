import { useState } from 'react';
import InventoryItem from './InventoryItem';

export default function HomePage( props ) {
console.log(props)
    return (
        <>
            <h2>Inventory</h2>
            <div className="title_container">
                {
                    props.inventory.map((item, index) => <InventoryItem item={item} changeInventory={props.changeInventory} inventory={props.inventory} number={index}/>)
                }
            </div>
            <button onClick={()=>increment()}>Add One
            </button>
        </>
    );
}
