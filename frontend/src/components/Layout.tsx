import { ReactNode, useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { Home, Database, Pill, Search, Users, Menu } from 'lucide-react'

interface LayoutProps {
  children: ReactNode
}

export default function Layout({ children }: LayoutProps) {
  const location = useLocation()
  const [sidebarOpen, setSidebarOpen] = useState(true)

  const navigation = [
    { name: 'Dashboard', href: '/', icon: Home },
    { name: 'Sjukdomar', href: '/diseases', icon: Database },
    { name: 'Läkemedel', href: '/medications', icon: Pill },
    { name: 'Symtomchecker', href: '/symptom-checker', icon: Search },
    { name: 'Patienter', href: '/patients', icon: Users },
  ]

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Sidebar */}
      <aside
        className={`fixed left-0 top-0 h-full bg-primary-900 text-white transition-all duration-300 ${
          sidebarOpen ? 'w-64' : 'w-20'
        }`}
      >
        <div className="flex items-center justify-between p-4 border-b border-primary-800">
          <h1 className={`font-bold text-xl ${sidebarOpen ? '' : 'hidden'}`}>
            Ögonsekreterare
          </h1>
          <button
            onClick={() => setSidebarOpen(!sidebarOpen)}
            className="p-2 rounded-lg hover:bg-primary-800"
          >
            <Menu className="w-6 h-6" />
          </button>
        </div>
        <nav className="mt-6 px-2">
          {navigation.map((item) => {
            const Icon = item.icon
            const isActive = location.pathname === item.href
            return (
              <Link
                key={item.name}
                to={item.href}
                className={`flex items-center gap-3 px-4 py-3 rounded-lg mb-1 transition-colors ${
                  isActive
                    ? 'bg-primary-800 text-white'
                    : 'text-primary-200 hover:bg-primary-800 hover:text-white'
                }`}
              >
                <Icon className="w-5 h-5 flex-shrink-0" />
                <span className={sidebarOpen ? '' : 'hidden'}>{item.name}</span>
              </Link>
            )
          })}
        </nav>
      </aside>

      {/* Main content */}
      <main
        className={`transition-all duration-300 ${
          sidebarOpen ? 'ml-64' : 'ml-20'
        }`}
      >
        <div className="p-8">{children}</div>
      </main>
    </div>
  )
}
