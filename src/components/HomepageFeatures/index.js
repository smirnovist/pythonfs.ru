import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Всегда в актуальном состоянии',
    Svg: require('@site/static/images/logo.svg').default,
    description: (
      <>
        Учебник всегда будет соответствовать последней стабильной версии Python.
      </>
    ),
  },
  {
    title: 'Все материалы доступны бесплатно',
    Svg: require('@site/static/images/logo.svg').default,
    description: (
      <>
        Учебник всегда будет доступен в полном объёме бесплатно.
      </>
    ),
  },
  {
    title: 'Обучение с нуля до профессионального уровня',
    Svg: require('@site/static/images/logo.svg').default,
    description: (
      <>
        Учебник написан так, чтобы любой желающий мог научиться программировать с нуля до профессионального уровня.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
