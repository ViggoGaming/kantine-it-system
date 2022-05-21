import { Table } from 'react-bootstrap';
import './App.css';

function EditFood_card(props: any) {
    return (
        <div>
            <Table striped bordered hover size="sm">
                <thead>
                    <tr>
                        <th>id</th>
                        <th>name</th>
                        <th>description</th>
                        <th>price</th>
                        <th>image</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{props.id}</td>
                        <td>{props.name}</td>
                        <td>{props.description}</td>
                        <td>{props.image}</td>
                        <td>{props.price}</td>
                    </tr>
                </tbody>
            </Table>
        </div>
    )
}

export default EditFood_card
