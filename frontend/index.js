import React from 'react';
import ReactDOM from "react-dom";
import Card from 'react-bootstrap/Card'
import ListGroupItem from "react-bootstrap/ListGroupItem";
import ListGroup from "react-bootstrap/ListGroup";
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"

class Activity extends React.Component {
    render() {
        return (
            <ListGroupItem>
                d
            </ListGroupItem>
        )
    }
}


class Events extends React.Component {
    render() {
        return (
            <p>content</p>
        )
    }
}


ReactDOM.render(
    <Row>
        <Col sm={6}>
            <Card>
                <Card.Header>
                    <Card.Title>Activity</Card.Title>
                </Card.Header>
                <ListGroup variant="flush">
                    <Activity/>
                </ListGroup>
            </Card>
        </Col>
        <Col sm={6}>
            <Card>
                <Card.Header>
                    <Card.Title>Upcoming events and tasks</Card.Title>
                </Card.Header>
                <Card.Body>
                    <Events/>
                </Card.Body>
            </Card>
            <Card className="mt-2">
                <Card.Header>
                    <h6 className="d-flex align-items-center justify-content-between">
                        <span>Team</span>
                        <a href="#" className="btn btn-sm btn-light border btn-icon">
                            <i className="bi bi-person-plus-fill"/>
                        </a>
                    </h6>
                </Card.Header>
            </Card>
        </Col>
    </Row>,
    document.getElementById('react')
);