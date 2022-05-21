import { Card, CardGroup, Col, Row } from 'react-bootstrap';
import './App.css';

function Food_card(props: any) {
    return (
        <div className="card">
            <img src={props.image} alt="" />
            <div className="card-body">
                <h2>{props.name}</h2>
                <p>
                    {props.description}
                </p>
                <h5>{props.price} kr.</h5>
            </div>
        </div>

    )
}

export default Food_card
