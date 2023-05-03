// import { useState } from "react";
import './inventory.css'

export default function InventoryItem( props ) {
    // const [copyAvailableOne, setCopiesAvailable] = useState(copiesAvailable)
    // console.log(changeInventory)
    // function checkoutTitle() {
    //     setCopiesAvailable(prevCopiesAvailable => prevCopiesAvailable - 1)
    // }
    function checkOut() {
        console.log(props.inventory)
        console.log(props.inventory[props.number])
        props.inventory[props.number]['copiesAvailable'] -= 1
        console.log(props.inventory[props.number])
        props.changeInventory(props.inventory) 
        console.log(props.inventory)
    }
    // console.log(props.inventory[props.number])
    return (
        <div className='card'>
            <h1>{props.item.title}</h1>
            <img src={props.item.imgUrl}/>
            <h2>Copies Available{props.item.copiesAvailable}</h2>
            <button onClick={()=> checkOut()}>Checkout</button>
        </div>
    )

}