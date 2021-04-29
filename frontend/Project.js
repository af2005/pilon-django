function ProjectApplication() {
    return (
        <div className="row">
            <div className="col-sm-6">
                <div className="card  my-2 ">
                    <div className="card-header">
                        <h6 className="mb-0">Activity</h6>
                    </div>
                    <div className="list-group-flush" id="homepage-activity">

                    </div>
                </div>
            </div>
            <div className="col-sm-6">
                <div className="card my-2">
                    <div className="card-header">
                        <h6 className="mb-0">Upcoming events and tasks</h6>
                    </div>
                    <div id="homepage-events" className="card-body">

                    </div>

                </div>
                <div className="card my-3">
                    <div className="card-header">
                        <h6 className="d-flex align-items-center justify-content-between">
                            <span>Team</span>
                            <a href="#" className="btn btn-sm btn-light border btn-icon">
                                <i className="bi bi-person-plus-fill"/>
                            </a></h6>
                    </div>
                    <div className="card-body">
                    </div>
                </div>

            </div>


        </div>
    );
}

