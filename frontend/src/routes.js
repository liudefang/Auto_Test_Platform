const NotFound = () => import('./views/common/404.vue');
const Login = () => import('./views/common/Login.vue');
const Home = () => import('./views/Home.vue');
const About = () => import('./views/About.vue');
const projectList = () => import('./views/Projectlist.vue');
const ProjectInfo = () => import('./views/Project.vue');
const ProjectTitle = () => import('./views/project/projectTitle/ProjectTitle.vue');
const globalHost = () => import('./views/project/global/Globalhost.vue');

let routes = [
    {
        path: '/login',
        component: Login,
        name: '',
        hidden: true,
        projectHidden: true
    },
    {
        path: '/404',
        component: NotFound,
        name: '',
        hidden: true,
        projectHidden: true
    },
    {
        path: '/',
        component: Home,
        name: '',
        projectHidden: true,
        children: [
            { path: '/projectList', component: projectList, iconCls:'el-icon-message', name: '项目列表'},
            // { path: '/robot', component: robot, iconCls:'fa fa-id-card-o', name: '消息机器人', meta: { keepAlive: false }},
            { path: '/about', component: About, iconCls:'fa fa-address-card', name: '关于我们'},
            ]
    },
    {
      path: '*',
      hidden: true,
      projectHidden: true,
      redirect: { path: '/404'}
    },
    {
      path: '/project/project=:project_id',
      component: ProjectInfo,
      name: '项目',
      hidden: true,
      children: [
        {
          path: '/ProjectTitle/project=:project_id', component: ProjectTitle, name: '项目概况', leaf: true
        },
        {
          path: '/GlobalHost/project=:project_id', component: globalHost, name: 'Host配置', leaf: true
        },

      ]
    }

];

export default routes;
