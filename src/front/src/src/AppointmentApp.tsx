import {BrowserRouter, Route, Routes} from 'react-router-dom';
import {LoginPage} from './auth/pages/LoginPage';
import AppointmentPage from './appointments/pages/Appointment';
import {QueryClient, QueryClientProvider} from 'react-query';
import {ReactQueryDevtools} from 'react-query/devtools';

const queryClient = new QueryClient({});

export default function AppointmentApp() {
  return (
    <BrowserRouter>
      <QueryClientProvider client={queryClient}>
        <div className="container">
          <Routes>
            <Route path="/auth/login" element={<LoginPage />}></Route>
            <Route path="/appointments" element={<AppointmentPage />}></Route>
          </Routes>
        </div>
        <ReactQueryDevtools initialIsOpen={false} />
      </QueryClientProvider>
    </BrowserRouter>
  );
}
