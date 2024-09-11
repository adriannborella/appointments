import React from 'react';
import {useFormik} from 'formik';
// import '../utils/styles.scss';

export function LoginPage() {
  const formik = useFormik({
    initialValues: {
      email: '',
      password: '',
    },
    onSubmit: (values) => {
      alert(JSON.stringify(values, null, 2));
    },
  });
  return (
    <form onSubmit={formik.handleSubmit}>
      <h3>Sign In</h3>
      <div className="mb-3">
        <label>Email address</label>
        <input
          type="email"
          name="email"
          className="form-control"
          placeholder="Enter email"
          onChange={formik.handleChange}
          value={formik.values.email}
        />
      </div>
      <div className="mb-3">
        <label>Password</label>
        <input
          type="password"
          name="password"
          className="form-control"
          placeholder="Enter password"
          onChange={formik.handleChange}
          value={formik.values.password}
        />
      </div>
      <div className="d-grid">
        <button type="submit" className="btn btn-primary">
          Submit
        </button>
      </div>
      {/* <p className="forgot-password text-right">
          Forgot <a href="#">password?</a>
        </p> */}
    </form>
  );
}
